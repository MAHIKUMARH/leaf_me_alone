from flask import Flask, render_template, request, redirect, session, url_for
import os
import uuid
import sqlite3
from datetime import datetime

import cv2
import numpy as np
from werkzeug.security import check_password_hash, generate_password_hash

from detector.vein_counter import count_veins


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
DATABASE = "database.db"

app.config["SECRET_KEY"] = "leaf_me_alone_secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# DATABASE
# ==========================================================

def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():

    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS leaves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image_path TEXT NOT NULL,
            vein_image_path TEXT NOT NULL,
            vein_count INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL COLLATE NOCASE UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    leaf_columns = {
        column[1]
        for column in connection.execute("PRAGMA table_info(leaves)").fetchall()
    }
    if "leaf_name" not in leaf_columns:
        connection.execute(
            "ALTER TABLE leaves ADD COLUMN leaf_name TEXT NOT NULL DEFAULT 'Unnamed leaf'"
        )

    connection.commit()
    connection.close()


init_db()


# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def home():

    connection = get_db()

    leaderboard = connection.execute(
        """
        SELECT name, leaf_name, vein_count
        FROM leaves
        ORDER BY vein_count DESC
        LIMIT 10
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        leaderboard=leaderboard,
        username=session.get("username")
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        password = request.form.get("password", "")

        if not name or not password:
            return render_template(
                "login.html",
                mode="signin",
                error="Enter both your name and password to continue."
            )

        connection = get_db()
        user = connection.execute(
            "SELECT name, password_hash FROM users WHERE name = ?",
            (name,)
        ).fetchone()
        connection.close()

        if user is None or not check_password_hash(user["password_hash"], password):
            return render_template(
                "login.html",
                mode="signin",
                error="That name and password do not match."
            )

        session["username"] = user["name"]
        return redirect("/")

    return render_template("login.html", mode="signin")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if len(name) < 2:
            return render_template(
                "login.html",
                mode="signup",
                error="Your name must contain at least 2 characters."
            )

        if len(password) < 6:
            return render_template(
                "login.html",
                mode="signup",
                error="Your password must contain at least 6 characters."
            )

        if password != confirm_password:
            return render_template(
                "login.html",
                mode="signup",
                error="The passwords do not match."
            )

        connection = get_db()
        existing_user = connection.execute(
            "SELECT id FROM users WHERE name = ?",
            (name,)
        ).fetchone()

        if existing_user is not None:
            connection.close()
            return render_template(
                "login.html",
                mode="signup",
                error="That name is already registered. Please sign in."
            )

        connection.execute(
            """
            INSERT INTO users (name, password_hash, created_at)
            VALUES (?, ?, ?)
            """,
            (
                name,
                generate_password_hash(password),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )
        connection.commit()
        connection.close()

        session["username"] = name
        return redirect("/")

    return render_template("login.html", mode="signup")


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return redirect("/login")

# ==========================================================
# ANALYZE LEAF
# ==========================================================

@app.route("/analyze", methods=["POST"])
def analyze():

    name = request.form.get("name", "").strip()
    leaf_name = request.form.get("leaf_name", "").strip()
    uploaded = request.files.get("image")

    if not name:
        return "Please enter your name."

    if not leaf_name:
        return "Please enter a name for this leaf."

    if uploaded is None or uploaded.filename == "":
        return "Please upload a leaf image."

    # ------------------------------------------------------
    # Read uploaded image
    # ------------------------------------------------------

    file_bytes = uploaded.read()

    if not file_bytes:
        return "The uploaded file is empty."

    data = np.frombuffer(
        file_bytes,
        dtype=np.uint8
    )

    image_data = cv2.imdecode(
        data,
        cv2.IMREAD_COLOR
    )

    if image_data is None:
        return (
            "Cannot read this image. "
            "Please upload JPG, JPEG, PNG, or WEBP."
        )

    # ------------------------------------------------------
    # Unique filename
    # ------------------------------------------------------

    image_id = uuid.uuid4().hex[:10]

    original_filename = (
        f"leaf_{image_id}.png"
    )

    original_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        original_filename
    )

    cv2.imwrite(
        original_path,
        image_data
    )

    # ------------------------------------------------------
    # PHASE 1 — VEIN DETECTION
    # ------------------------------------------------------

    vein_count, vein_mask, visualization = count_veins(
        image_data
    )

    # ------------------------------------------------------
    # Save detected-vein image
    # ------------------------------------------------------

    vein_filename = (
        f"leaf_{image_id}_veins.png"
    )

    vein_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        vein_filename
    )

    cv2.imwrite(
        vein_path,
        visualization
    )

    # ------------------------------------------------------
    # SAVE TO DATABASE
    # ------------------------------------------------------

    connection = get_db()

    connection.execute(
        """
        INSERT INTO leaves
        (
            name,
            leaf_name,
            image_path,
            vein_image_path,
            vein_count,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            leaf_name,
            original_path.replace("\\", "/"),
            vein_path.replace("\\", "/"),
            int(vein_count),
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    connection.commit()
    connection.close()

    # ------------------------------------------------------
    # RESULT PAGE
    # ------------------------------------------------------

    return render_template(
        "result.html",
        name=name,
        leaf_name=leaf_name,
        image_path="/" + original_path.replace("\\", "/"),
        vein_image_path="/" + vein_path.replace("\\", "/"),
        vein_count=vein_count
    )


# LEAF COLLECTION
# ==========================================================

@app.route("/leaves")
def leaves():

    connection = get_db()

    # All leaves for the collection
    leaves = connection.execute(
        """
        SELECT *
        FROM leaves
        ORDER BY created_at DESC
        """
    ).fetchall()

    # Highest vein counts first
    leaderboard = connection.execute(
        """
        SELECT name, leaf_name, vein_count
        FROM leaves
        ORDER BY vein_count DESC
        LIMIT 10
        """
    ).fetchall()

    connection.close()

    return render_template(
        "leaves.html",
        leaves=leaves,
        leaderboard=leaderboard
    )

# ==========================================================
# PERSONAL DASHBOARD
# ==========================================================
@app.route("/dashboard")
def dashboard():
    name = session.get("username", "").strip()

    if not name:
        return redirect("/login")

    connection = get_db()

    my_leaves = connection.execute(
        """
        SELECT *
        FROM leaves
        WHERE LOWER(name) = LOWER(?)
        ORDER BY created_at DESC
        """,
        (name,)
    ).fetchall()

    connection.close()

    total_leaves = len(my_leaves)
    total_veins = sum(leaf["vein_count"] for leaf in my_leaves)

    if my_leaves:
        best_leaf = max(my_leaves, key=lambda leaf: leaf["vein_count"])
        best_count = best_leaf["vein_count"]
    else:
        best_leaf = None
        best_count = 0

    if best_count <= 5:
        highest_rarity = "DIVINE"
        rarity_emoji = "✨"
    elif best_count < 500:
        highest_rarity = "BASE"
        rarity_emoji = "🌱"
    elif best_count < 2000:
        highest_rarity = "COMMON"
        rarity_emoji = "🍃"
    elif best_count < 5000:
        highest_rarity = "RARE"
        rarity_emoji = "💎"
    elif best_count < 10000:
        highest_rarity = "EPIC"
        rarity_emoji = "⚡"
    elif best_count < 15000:
        highest_rarity = "LEGENDARY"
        rarity_emoji = "🔥"
    else:
        highest_rarity = "MYTHIC"
        rarity_emoji = "👑"

    return render_template(
        "dashboard.html",
        name=name,
        leaves=my_leaves,
        total_leaves=total_leaves,
        total_veins=total_veins,
        best_leaf=best_leaf,
        best_count=best_count,
        highest_rarity=highest_rarity,
        rarity_emoji=rarity_emoji
    )


@app.route("/dashboard/<name>")
def dashboard_by_name(name):
    session_name = session.get("username", "").strip()
    if not session_name:
        return redirect("/login")

    if session_name.lower() != name.strip().lower():
        return redirect("/dashboard")

    return redirect("/dashboard")

@app.route("/delete/<int:leaf_id>", methods=["POST"])
def delete_leaf(leaf_id):

    connection = get_db()

    # Find the leaf first
    leaf = connection.execute(
        """
        SELECT image_path, vein_image_path
        FROM leaves
        WHERE id = ?
        """,
        (leaf_id,)
    ).fetchone()

    if leaf is None:
        connection.close()
        return "Leaf not found."

    # Delete database record
    connection.execute(
        """
        DELETE FROM leaves
        WHERE id = ?
        """,
        (leaf_id,)
    )

    connection.commit()
    connection.close()

    # Delete original image
    image_path = leaf["image_path"]

    if os.path.exists(image_path):
        os.remove(image_path)

    # Delete detected-vein image
    vein_image_path = leaf["vein_image_path"]

    if os.path.exists(vein_image_path):
        os.remove(vein_image_path)

    return redirect("/leaves")
# ==========================================================
# START APPLICATION
# ==========================================================

if __name__ == "__main__":

    init_db()

    app.run(
        debug=True
    )