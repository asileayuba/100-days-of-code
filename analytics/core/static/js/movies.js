$(document).ready(function() {
    // Check if DataTable is already initialized
    if ($.fn.dataTable.isDataTable('#datatable')) {
        $('#datatable').DataTable().clear().destroy();
    }

    // Initialize DataTable with the columns to be displayed
    const dataTable = $('#datatable').DataTable({
        "paging": true,  // Enable paging
        "searching": true,
        "ordering": true,
        "info": true,
        "columns": [
            { title: "ID", data: "id" },       // Expecting 'id' here
            { title: "Title", data: "title" }, // Expecting 'title' here
            { title: "Year", data: "year" },   // Expecting 'year' here
            { title: "Rating", data: "rating" }, // Expecting 'rating' here
            { title: "Votes", data: "votes" }  // Expecting 'votes' here
        ]
    });

    // Fetch data for the DataTable (from /api/movies_with_ratings/)
    fetch('/api/movies_with_ratings/')
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Debug log

        if (data && data.data) {
            // Add data to the DataTable
            dataTable.clear().rows.add(data.data).draw();
        } else {
            console.error('Invalid data structure:', data);
        }
    })
    .catch(error => console.error('Error:', error));
});
