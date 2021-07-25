<?php 
$server= 'localhost:3307';
$user='root';
$pass='';
$db="restaurante";
$conexion1= mysqli_connect($server,$user,$pass,$db);

$nombre=$_POST["txtnombre"];
$dni=$_POST["txtdni"];
$plato=$_POST["txtplato"];
$bebida=$_POST["txtbebida"];
if(isset($_POST["btnregistrar"])){
    $registro="INSERT INTO pedido values('$dni','$nombre','$plato','$bebida')";
    mysqli_query($conexion1,$registro);
    header("Location:restaurante.html"); 
}

?>
<style>
    table{
        border:1px solid black
    }
    td{
        padding: 5px 15px;
        border:1px solid black
    }
</style>
<div>
    <table>
        <tr>
            <td>DNI</td>
            <td>NOMBRE</td>
            <td>PLATO PEDIDO</td>
            <td>BEBIDA</td>
        </tr>
        <?php 
        $consulta="SELECT * FROM pedido";
        $resultado=mysqli_query($conexion1,$consulta);
        while($fila=mysqli_fetch_assoc($resultado)){
        ?>    
        
        <tr>
            <td><?php echo $fila['DNI']?></td>
            <td><?php echo $fila['NOMBRE']?></td>
            <td><?php echo $fila['PLATO']?></td>
            <td><?php echo $fila['BEBIDA']?></td>
        </tr>
        <?php 
        }
        ?>
    </table>
</div>