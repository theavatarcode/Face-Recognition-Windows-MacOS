<?php
    $servername = "localhost";
    $username = "root";
    $password = "";

    try {
        $conn = new PDO("mysql:host=$servername;dbname=data_db", $username, $password);
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        // echo "Connected successfully";
    } catch(PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DataTable</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.12.1/css/jquery.dataTables.min.css">
    
    <link rel="stylesheet" href="node_modules/@fortawesome/fontawesome-free/css/all.min.css">
</head>
<body class="bg-secondary">
    <?php include_once('navbar.php') ?>

    <div class="container mt-5 text-center">
        <div class="card mt-5 p-5" style="width:100%">
        <table id="example" class="table table-hover table-responsive">
            <thead class="table-light mt-5">
                <tr class="table">
                    <th>Name</th>
                    <th>Student-ID</th>
                    <th>Class-ID</th>
                    <th>Class</th>
                    <th>Date</th>
                    <th>Time</th>
                    
                </tr>
            </thead>
            <tbody>
            <?php
                $stmt = $conn->query("SELECT * FROM tb_students");
                $stmt->execute();

                $users = $stmt->fetchAll();
                foreach($users as $user){     
            ?>  
                <tr>
                    
                    <td class="table-success"><?php echo $user['name']?></td>
                    <td class="table-success"><?php echo $user['studentid']?></td>
                    <td class="table-secondary"><?php echo $user['classid']?></td>
                    <td class="table-secondary"><?php echo $user['class']?></td>
                    <td class="table-secondary"><?php echo $user['date']?></td>
                    <td class="table-danger"><?php echo $user['time']?></td> 
                    
                </tr>
                
            <?php
                };
            ?>
            </tbody>
        </table>
        </div>
    </div>
    
        
    
    
    <script src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
    <script src="https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/fixedheader/3.2.4/js/dataTables.fixedHeader.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
    
    <script type="text/javascript">
      $(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#example thead tr').clone(true).addClass('filters').appendTo( '#example thead' );
    var table = $('#example').DataTable( {
        orderCellsTop: true,
        // fixedHeader: true,
        responsive: true,
        
        initComplete: function() {
            var api = this.api();
            // For each column
            api.columns().eq(0).each(function(colIdx) {
                // Set the header cell to contain the input element
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html( '<input type="text" style="width:100%" placeholder="'+title+'" />' );
                // On every keypress in this input
                $('input', $('.filters th').eq($(api.column(colIdx).header()).index()) )
                    .off('keyup change')
                    .on('keyup change', function (e) {
                        e.stopPropagation();
                        // Get the search value
                        $(this).attr('title', $(this).val());
                        var regexr = '({search})'; //$(this).parents('th').find('select').val();
                        var cursorPosition = this.selectionStart;
                        // Search the column for that value
                        api
                            .column(colIdx)
                            .search((this.value != "") ? regexr.replace('{search}', '((('+this.value+')))') : "", this.value != "", this.value == "")
                            .draw();
                        $(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
                    });
            });
        }
    } );
} );
    </script>

    
    <script src="node_modules/popper.js/dist/umd/popper.min.js"></script>
    
</body>
</html>