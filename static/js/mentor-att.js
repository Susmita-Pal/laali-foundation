var ctx = document.getElementById('myChart').getContext("2d");
var label_val = 10
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Student A', 'Student B', 'Student C', 'Student D', 'Student E'],
        datasets: [
            {
            label: 'Total Number of Classes:'.concat(label_val.toString()),
            data: [2, 9, 8, 5, 4],
            backgroundColor: [
                'rgba(75, 192, 192, 0.8)'
            ],
            borderColor: [
                'rgba(175, 92, 192, 0.8)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: false,
        layout: {
            padding:{
            top:50,
            left:50,
            right:0,
            bottom:0,
            },
        },
        plugins:{
        title: {
            display:true,
            text:"Bar Chart",
        },
    },
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});