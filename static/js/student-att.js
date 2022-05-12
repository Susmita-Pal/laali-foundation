var ctx = document.getElementById('myChart').getContext("2d");

var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Present', 'Absent'],
        datasets: [{
            label: 'No of Classes',
            data: [24,7],
            backgroundColor: [
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 99, 132, 0.8)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: false,
        layout: {
            padding:{
            top:50,
            left:400,
            right:0,
            bottom:0,
            },
        },
        plugins:{
        title: {
            display:true,
            text:"Session Attendance",
        },
    },
    }
});