const totalViewChart = document.getElementById('total-views-chart');
const revenueChart = document.getElementById('revenue-chart');
const growthRateChart = document.getElementById('growth-rate-chart');
const subscriberCountChart = document.getElementById('subscriber-count');
const trafficSourcesElement = document.getElementById('traffic-sources');

new Chart(totalViewChart, {
    type: 'line',
    data: {
        labels: ['Aug', 'Sep', 'Oct', 'Dec', 'Jan'],
        datasets: [{
            label: '# of Views',  
            data: [12545, 19512, 37897, 24574, 29564],
            borderWidth: 1
        }]
    },  
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

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
            y: {
                beginAtZero: true
            }
        }
    }
});

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
            y: {
                beginAtZero: true
            }
        }
    }
});

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
        responsive: false,  // Disable auto resizing
        maintainAspectRatio: false,  // Allow custom dimensions
        plugins: {
            legend: {
                display: true,
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        return tooltipItem.label + ': ' + tooltipItem.raw + '%';
                    }
                }
            }
        }
    }
});


$(document).ready(function() {
    $('#datatable').DataTable({
        "paging": true,
        "searching": true,
        "ordering": true,
        "info": true
    });
});
