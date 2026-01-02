function captureElement(element, callback) {
    const originalWidth = element.style.width;
    const originalMaxWidth = element.style.maxWidth;

    // Force full width
    element.style.width = element.scrollWidth + "px";
    element.style.maxWidth = "none";

    html2canvas(element, {
        scale: 2,
        windowWidth: element.scrollWidth,
        scrollX: 0,
        scrollY: 0
    }).then(canvas => {
        callback(canvas);

        // Restore styles
        element.style.width = originalWidth;
        element.style.maxWidth = originalMaxWidth;
    });
}

function downloadImage() {
    const table = document.getElementById("timetable-table");

    captureElement(table, canvas => {
        const link = document.createElement("a");
        link.download = "timetable.png";
        link.href = canvas.toDataURL("image/png");
        link.click();
    });
}

function downloadPDF() {
    const table = document.getElementById("timetable-table");
    const { jsPDF } = window.jspdf;

    captureElement(table, canvas => {
        const imgData = canvas.toDataURL("image/png");

        const pdf = new jsPDF("landscape", "pt", "a4");
        const pageWidth = pdf.internal.pageSize.getWidth();
        const pageHeight = pdf.internal.pageSize.getHeight();

        const imgWidth = pageWidth;
        const imgHeight = (canvas.height * imgWidth) / canvas.width;

        pdf.addImage(imgData, "PNG", 0, 20, imgWidth, imgHeight);
        pdf.save("timetable.pdf");
    });
}



document.querySelectorAll("td").forEach(cell => {
    cell.addEventListener("mouseenter", () => {
        cell.style.zIndex = 10;
    });
    cell.addEventListener("mouseleave", () => {
        cell.style.zIndex = 1;
    });
});

