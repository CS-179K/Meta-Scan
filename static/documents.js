window.addEventListener('load', function() {
    fetch('/document-output')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#data-table tbody');
            tableBody.innerHTML = ''; // Clear any existing content

            data.data.forEach(item => {
                const row = document.createElement('tr');
                const labelCell = document.createElement('td');
                const valueCell = document.createElement('td');

                labelCell.textContent = item.label;
                valueCell.textContent = item.value;

                row.appendChild(labelCell);
                row.appendChild(valueCell);
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching document data:', error));
});
