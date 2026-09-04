import cv2
import numpy as np

try:
    from skimage.morphology import skeletonize
except ImportError:
    raise ImportError(
        "scikit-image is required. Run: "
        "python -m pip install scikit-image"
    )


def largest_component(binary):
    count, labels, stats, _ = cv2.connectedComponentsWithStats(
        binary, 8
    )

    if count <= 1:
        return binary

    largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])

    return np.where(
        labels == largest,
        255,
        0
    ).astype(np.uint8)


def get_leaf_mask(image):
    """
    Isolate the main leaf from the background.
    """

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green vegetation mask
    mask = cv2.inRange(
        hsv,
        np.array([20, 20, 15], dtype=np.uint8),
        np.array([100, 255, 255], dtype=np.uint8)
    )

    mask = largest_component(mask)

    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (9, 9)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel,
        iterations=1
    )

    return largest_component(mask)


def enhance_leaf(image, leaf_mask):
    """
    Convert to grayscale and enhance local contrast using CLAHE.
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.5,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    enhanced = cv2.GaussianBlur(
        enhanced,
        (3, 3),
        0
    )

    enhanced = cv2.bitwise_and(
        enhanced,
        enhanced,
        mask=leaf_mask
    )

    return enhanced


def extract_veins(enhanced, leaf_mask):
    """
    Extract dark vein structures from the enhanced leaf.
    """

    # Black-hat highlights dark structures surrounded by brighter tissue.
    responses = []

    for size in (5, 9, 13):
        kernel = cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE,
            (size, size)
        )

        response = cv2.morphologyEx(
            enhanced,
            cv2.MORPH_BLACKHAT,
            kernel
        )

        response = cv2.bitwise_and(
            response,
            response,
            mask=leaf_mask
        )

        responses.append(
            response.astype(np.float32)
        )

    combined = (
        0.25 * responses[0]
        +
        0.50 * responses[1]
        +
        0.25 * responses[2]
    )

    combined = cv2.normalize(
        combined,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    # Adaptive threshold
    binary = cv2.adaptiveThreshold(
        combined,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        -2
    )

    binary = cv2.bitwise_and(
        binary,
        leaf_mask
    )

    # Remove tiny noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (3, 3)
    )

    binary = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel,
        iterations=1
    )

    # Connect small gaps
    binary = cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=1
    )

    return binary


def skeletonize_veins(vein_mask):
    skeleton = skeletonize(
        vein_mask > 0
    )

    return (
        skeleton.astype(np.uint8) * 255
    )


def count_branch_points(skeleton):
    """
    Count endpoints and branch locations on the skeleton.

    We use endpoints as the main measure because each visible
    secondary vein generally terminates near the leaf edge.
    """

    sk = skeleton > 0

    kernel = np.ones(
        (3, 3),
        dtype=np.uint8
    )

    neighbour_count = cv2.filter2D(
        sk.astype(np.uint8),
        cv2.CV_16U,
        kernel
    ) - sk.astype(np.uint8)

    # Pixels with exactly one neighbour = endpoints
    endpoints = (
        sk &
        (neighbour_count == 1)
    )

    # Group nearby endpoint pixels
    endpoint_image = (
        endpoints.astype(np.uint8) * 255
    )

    endpoint_image = cv2.dilate(
        endpoint_image,
        np.ones((5, 5), np.uint8),
        iterations=1
    )

    count, labels, stats, _ = cv2.connectedComponentsWithStats(
        endpoint_image,
        8
    )

    endpoint_count = 0

    for i in range(1, count):
        area = stats[
            i,
            cv2.CC_STAT_AREA
        ]

        if area >= 8:
            endpoint_count += 1

    return endpoint_count


def draw_veins(image, skeleton):
    """
    Draw detected vein structure in RED.
    """

    output = image.copy()

    red_pixels = skeleton > 0

    # OpenCV uses BGR, so this is RED.
    output[red_pixels] = (
        0,
        0,
        255
    )

    return output


def count_veins(image):
    """
    Main function used by Flask.

    Returns:

        vein_count
        vein_mask
        visualization
    """

    if image is None:
        return (
            0,
            np.zeros((1, 1), dtype=np.uint8),
            image
        )

    # -----------------------------------------
    # 1. Isolate leaf
    # -----------------------------------------

    leaf_mask = get_leaf_mask(image)

    leaf_area = cv2.countNonZero(
        leaf_mask
    )

    if leaf_area == 0:
        print("Leaf mask could not be detected.")

        return (
            0,
            np.zeros(
                image.shape[:2],
                dtype=np.uint8
            ),
            image
        )

    # -----------------------------------------
    # 2. CLAHE enhancement
    # -----------------------------------------

    enhanced = enhance_leaf(
        image,
        leaf_mask
    )

    # -----------------------------------------
    # 3. Extract veins
    # -----------------------------------------

    vein_mask = extract_veins(
        enhanced,
        leaf_mask
    )

    # -----------------------------------------
    # 4. Skeletonize
    # -----------------------------------------

    skeleton = skeletonize_veins(
        vein_mask
    )

    # -----------------------------------------
    # 5. Count visible vein branches
    # -----------------------------------------

    vein_count = count_branch_points(
        skeleton
    )

    # -----------------------------------------
    # 6. Draw result
    # -----------------------------------------

    visualization = draw_veins(
        image,
        skeleton
    )

    print("--------------------------------")
    print("LEAF ANALYSIS")
    print("--------------------------------")
    print(
        "Leaf pixels:",
        leaf_area
    )
    print(
        "Vein pixels:",
        cv2.countNonZero(vein_mask)
    )
    print(
        "Skeleton pixels:",
        cv2.countNonZero(skeleton)
    )
    print(
        "Veins detected:",
        vein_count
    )
    print("--------------------------------")

    return (
        int(vein_count),
        vein_mask,
        visualization
    )