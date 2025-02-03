$(document).ready(function() {
    // Check if DataTable is already initialized
    if ($.fn.dataTable.isDataTable('#datatable')) {
        $('#datatable').DataTable().clear().destroy();
    }

    // Initialize DataTable
    const dataTable = $('#datatable').DataTable({
        "paging": true,  // Enable paging
        "pageLength": 3,  // Show only 3 rows per page
        "searching": true,
        "ordering": true,
        "info": true,
        "columns": [
            { title: "ID", data: "ID" },
            { title: "Title", data: "Title" },
            { title: "Year", data: "Year" }
        ]
    });

    // Fetch data for the DataTable
    fetch('/api/datatable_api/')
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Debug log
            dataTable.clear().rows.add(data).draw();  // Add data to the table
        })
        .catch(error => console.error('Error:', error));
});
