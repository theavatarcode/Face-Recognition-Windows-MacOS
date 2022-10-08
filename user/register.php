<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>REGISTER</title>
    <link rel="stylesheet" href="node_modules/bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="node_modules/@fortawesome/fontawesome-free/css/all.min.css">
</head>
<body class="bg-secondary">
    <?php include_once('navbar.php')?>
    


    <div class="container-sm d-flex justify-content-center text-dark mt-5">

        <div class="card mt-5" style="width: 80%;">
            <h1 class="card-header text-center ">REGISTER</h1>
            <div class="card-body">
                <form class="p-3">
                <div class="input-group mb-3">
                    <span class="input-group-text" id="inputGroup-sizing-default"><i class="fa-solid fa-user"></i></span>
                    <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Username">
                </div>
                <div class="input-group mb-3">
                    <span class="input-group-text" id="inputGroup-sizing-default"><i class="fa-solid fa-key"></i></span>
                    <input type="password" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Password">
                </div>

                <div class="input-group mb-3">
                    <span class="input-group-text" id="inputGroup-sizing-default"><i class="fa-solid fa-key"></i></span>
                    <input type="password" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Confirm-Password">
                </div>

                <div class="input-group mb-3">
                    <span class="input-group-text" id="inputGroup-sizing-default"><i class="fa-solid fa-envelope"></i></span>
                    <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Email">
                </div>
                <div class="input-group mb-3">
                    <span class="input-group-text" id="inputGroup-sizing-default"><i class="fa-solid fa-id-card"></i></span>
                    <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Student-id">
                </div>

                <select class="form-select mb-3" aria-label="Default select example">
                    <option selected>Role</option>
                    <option value="1">Student</option>
                    <option value="2">Teacher</option>
                    <option value="3">Parent</option>
                </select>
                <div class="d-grid gap-2">
                    
                    <button class="btn btn-primary" type="button">REGISTER</button>
                    
                    
                </div>
                
                </form> 
            </div>
        
        </div>
    
    </div>
   

    
    
        

    <script src="node_modules/jquery/dist/jquery.min.js"></script>
    <script src="node_modules/popper.js/dist/umd/popper.min.js"></script>
    <script src="node_modules/bootstrap/dist/js/bootstrap.min.js"></script>
</body>
</html>