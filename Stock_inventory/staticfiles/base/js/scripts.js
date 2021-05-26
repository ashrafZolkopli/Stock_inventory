up.compiler('#layoutSidenav_nav', function (element) {
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
})

up.compiler('.content_container', function (element) {
    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

    const stock_table = document.getElementById('stock_table');
    if (stock_table) {
        new simpleDatatables.DataTable(stock_table, {
            footer: true
        });
    }
})