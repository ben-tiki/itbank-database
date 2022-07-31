// using jquery apply pagination to the table with id "query_table"
$(document).ready(function() {
    $('#query_table').DataTable({
        "paging": true,
        // choose max number of rows per page
        "pageLength": 25,
        "lengthChange": false,
        "searching": false,
        "ordering": false,
        "info": true,
        "autoWidth": false
    });
}
);
