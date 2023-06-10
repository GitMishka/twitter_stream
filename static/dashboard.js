function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const oldRow = document.getElementById('data-row');
            if (oldRow) {
                oldRow.remove();
            }

            const newRow = document.createElement('tr');
            newRow.id = 'data-row';

            for (let key in data) {
                const newCell = document.createElement('td');
                newCell.textContent = data[key];
                newRow.appendChild(newCell);
            }

            const table = document.getElementById('data');
            table.appendChild(newRow);
        });
}

setInterval(fetchData, 1000);
