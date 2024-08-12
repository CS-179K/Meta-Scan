document.getElementById('viewDocuments').addEventListener('click', function() {
    document.getElementById('loader').style.display = 'block';
    setTimeout(function() {
        document.getElementById('loader').style.display = 'none';
        alert('Moving to database to view stored documents!');
    }, 2000);
});

document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function() {
    if (this.files && this.files.length > 0) {
        alert('File selected: ' + this.files[0].name);
    }
});
