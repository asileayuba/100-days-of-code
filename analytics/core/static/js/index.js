const totalViewChart = document.getElementById('total-views-chart');
const revenueChart = document.getElementById('revenue-chart');
const growthRateChart = document.getElementById('growth-rate-chart');
const subscriberCountChart = document.getElementById('subscriber-count');
const trafficSourcesElement = document.getElementById('traffic-sources');

// Fetch total views data
fetch('/api/total_views')
.then(res => res.json())
.then(data => {
    if (totalViewChart) {
        new Chart(totalViewChart, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: '# of Views',
                    data: data.data,
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }
})
.catch(error => console.error("Error fetching total views:", error));

// Subscriber Count Chart
if (subscriberCountChart) {
    new Chart(subscriberCountChart, {
        type: 'line',
        data: {
            labels: ['Aug', 'Sep', 'Oct', 'Dec', 'Jan'],
            datasets: [{
                label: 'Subscribers',
                data: [12, 19, 3, 5, 2],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// Revenue Chart
if (revenueChart) {
    new Chart(revenueChart, {
        type: 'line',
        data: {
            labels: ['Aug', 'Sep', 'Oct', 'Dec', 'Jan'],
            datasets: [{
                label: 'Revenue',
                data: [255, 280, 290, 179, 512],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// Traffic Sources Pie Chart
if (trafficSourcesElement) {
    new Chart(trafficSourcesElement, {
        type: 'pie',
        data: {
            labels: ['Direct', 'Referral', 'Social Media', 'Organic Search'],
            datasets: [{
                data: [55, 15, 20, 10],
                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e'],
                hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#f1b42e'],
                hoverBorderColor: "rgba(234, 236, 244, 1)"
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: true, position: 'top' },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            let index = tooltipItem.dataIndex;
                            return tooltipItem.chart.data.labels[index] + ': ' + tooltipItem.raw + '%';
                        }
                    }
                }
            }
        }
    });
}

$(document).ready(function() {
    // Initialize DataTable
    const dataTable = $('#datatable').DataTable({
        "paging": true,
        "searching": true,
        "ordering": true,
        "info": true,
        "columns": [
            { title: "Title" },
            { title: "Views" },
            { title: "Likes" },
            { title: "Comments" }
        ]
    });

    // Fetch data for the DataTable
    fetch('/api/datatable_api/')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Debug log
            dataTable.clear().rows.add(data).draw(); // Add this line to populate the table
        })
        .catch(error => console.error('Error:', error));
});
