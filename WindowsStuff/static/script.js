
document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function() {
    if (this.files && this.files.length > 0) {
        var formData = new FormData();
        formData.append('file', this.files[0]);

        var checkboxes = document.querySelectorAll('input[name="checkbox"]:checked');
        checkboxes.forEach(function(checkbox) {
            formData.append('checkbox', checkbox.value);
        });

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            beforeSend: function() {
                document.getElementById('loader').style.display = 'block';
            },
            success: function(response) {
                document.getElementById('loader').style.display = 'none';
                alert('File uploaded successfully.');
                // Redirect to the view documents page
                window.location.href = '/view';
            },
            error: function() {
                document.getElementById('loader').style.display = 'none';
                alert('An error occurred while uploading the file.');
            }
        });
    }
});

document.getElementById('viewDocuments').addEventListener('click', function() {
    // Show loader while fetching data
    document.getElementById('loader').style.display = 'block';

    // Redirect to the /view endpoint after a short delay
    setTimeout(function() {
        document.getElementById('loader').style.display = 'none';
        window.location.href = '/view';
    }, 500);
});

