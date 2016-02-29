<?phpclass connexion
{

private var $conn;

public function __construct__(){
{
	try
	{
	$this->conn = new PDO('mysql:host=E145617E;dbname=E145617E;charset=utf8','E145617E','E145617E',);
	}
	catch(Exception $e)
	{
		die('Erreur : '. e->getMessage());
	}

public function get_installations($nom_commune)
{
	$ret = $this->conn->querry('SELECT * from pages where (nom_commune = nom_commune)');
	return $ret;
}


