(() => {
    const input = document.getElementById("leaf-image");
    const fileName = document.getElementById("leaf-file-name");

    if (!input || !fileName) {
        return;
    }

    input.addEventListener("change", () => {
        fileName.textContent = input.files && input.files.length > 0
            ? input.files[0].name
            : "No image selected";
    });
})();