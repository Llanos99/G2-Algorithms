#include <algorithm>
#include <bits/stdc++.h>
#include <cstdio>
#include <sstream>
#include <vector>

// using namespace std : Sirve para que el compilador reconozca las
// funciones/clases/variables que estamos creando en caso de que haya una
// sobrecarga de la funcion en otra libreria. namespace definie el contexto en
// el cual nuestras funciones/variables/clases han sido creadas. i.e, define un
// scope.

using namespace std;

// Se utiliza para hacer un separado entre los niveles del arbol cuando imprimamos.
#define COUNT 4;

// Los Struct son clases de acceso publico por default, las "class" como tal son
// de acceso privado. Creamos el struct Node para el Binary Search Tree.

struct Node {

  int data; // Valor del nodo.
  // Puntero a los hijos de un nodo.
  struct Node *left;
  struct Node *right;
  // Creamos una bandera para determinar cuales son los nodos que necesitamos
  // para llegar al nodo buscado.
  bool is_needed;
  string direction; //Para determinar si el nodo esta a la izquierda o derecha del predecesor.

  //Constructor del Nodo.
  Node(int node_data) {
    this->data = node_data;
    this->left = NULL;
    this->right = NULL;
    this->is_needed = false;
    this->direction = "";
  }
};

vector<struct Node *> list_nodes; // ArrayList que contiene los nodos que se visitan en el camino de busqueda.
vector<string> moves;             // Movimientos necesarios para llegar hasta el elemento buscado.

// Con esta funcion averiguamos si el elemento buscado esta o no en el BST.
// Importante recalcar que a pesar de que un elemento no este, este metodo 
// guarda la informacion sobre DONDE deberia estar el elemento en el BST.

bool iterativeSearch(struct Node *root, int key) {
  while (root != NULL) {
    if (key > root->data) {       // Vamos al hijo derecho.
      root->is_needed = true;     // El nodo es parte del camino al elemento buscado.
      list_nodes.push_back(root); // Lo anadimos a nuestro camino.
      moves.push_back("Derecha"); // Le asignamos el movimiento "hacia la derecha" en el arbol.
      root = root->right;           //  Actualizamos al hijo derecho.
      root->direction = "Derecha";  // Le asignamos al nuevo nodo la direccion derecha.

    } else if (key < root->data) {    // Vamos al hijo izquierdo.
      root->is_needed = true;         // El nodo es parte del camino al elemento buscado.
      list_nodes.push_back(root);   // Lo anadimos al camino.
      moves.push_back("Izquierda"); // Le asignamos el movimiento "hacia la izquierda" en el arbol.
      root = root->left;              // Actualizamos al hijo izquierdo.
      root->direction = "Izquierda";  // Le asignamos al nuevo nodo la direccion izquierda.

    } else {                          // Si el elemento se encuentra, lo anadimos al camino y lo marcamos como necesario.
      list_nodes.push_back(root);
      root->is_needed = true;
      return true;
    }
  }
  return false;                     // El elemento no fue en econtrado en el BST.
}

// Creating a new node is not necessary if you have already created a struct
// constructor for Node struct.

/* struct Node *newNode(int item) {
  struct Node *temp = new Node(item);
  temp->data = item;
  temp->left = temp->right = NULL;
  return temp;
} */

// Funcion de insercion en el BST. Debe implementar las reglas de un BST.

static Node *insert(struct Node *node, int data) {

  // Si el arbol esta vacio, creamos la raiz con el valor dado y retornamos.
  if (node == NULL) {
    struct Node *ptr = new Node(data);
    return ptr;
  }
  // Si el valor del nodo dado es < que data, lo asignamos como un hijo izquierdo.
  if (data < node->data) {
    node->left = insert(node->left, data);
  }
  // Si el valor del nodo dado es > que data, lo asignamos como un hijo derecho.
  else if (data > node->data) {
    node->right = insert(node->right, data);
  }
  // Retornamos el nodo, pues este ya tiene posicion asignada en el arbol.
  return node;

}

// Hacemos una representacion grafica del arbol nivel por nivel.
// Para ello, hacemos un recorrido in-order del arbol, pero al reves, es decir (derecha-raiz-izquierda).
// Para lo anterior, usamos recursion.

// Complejidad : Como vamos a imprimir el arbol, vamos a recorrer todos los nodos del arbol una unica vez,
// de modo que printTree tiene una complejidad de orden O(n), donde n = # Nodos del arbol. 

void printTree(struct Node *root, int level) {

  if (root == NULL) {
    // Si la raiz es nula, no hacemos nada, pues no hay arbol que imprimir.
    return;
  }

  level += COUNT;   // Para hacer una separacion entre los niveles del arbol.

  // Implementamos el recorrido in-order inverso.

  printTree(root->right, level);  // Visitamos el nodo que esta mas a la derecha.

  // Sirve para crear un espaciado adecuado para imprimir el arbol.

  int ptr = COUNT;
  for (int p = ptr; p < level; p++) {
    cout << " ";
  }

  if(root->is_needed){              // Si el nodo actual esta en el camino, lo imprimimos con su respectiva direccion.
    if(root->direction == "Derecha"){
      cout << "⬈" <<root->data << "\n";
    }else if(root->direction == "Izquierda"){
      cout << "⬊" <<root->data << "\n";
    }else if(root->direction == ""){
      cout << "🠮 " <<root->data << "\n";
    }
  }
  else{
    cout << " " <<root->data << "\n";   // Si el nodo actual no esta en el camino, imprimimos el nodo pero sin direccion.
  }

  printTree(root->left, level);   // Completamos el recorrido del arbol, visitando el nodo que esta a la izquierda.

}

// Funcion para imprimir en consola los nodos que se recorren hasta llegar al nodo buscado.

void path_nodes(vector<struct Node *> nodes) {
  for (int i = 0; i < nodes.size(); i++) {
    if (nodes.at(i)->is_needed == true) {
      if (i == nodes.size() - 1) {
        cout << nodes.at(i)->data;
      } else {
        cout << nodes.at(i)->data << "->";
      }
    }
  }
  cout << "\n";
}

// Funcion para imprimir los movimientos necesarios en el arbol hasta llegar al nodo buscado.

void path_moves(vector<string> path){
  for(int i = 0; i < path.size(); i++){
    if(i == path.size()-1){
      cout << path.at(i);
    }else{
      cout << path.at(i) << "->";
    }
  }
  cout << "\n";
}

// Programa de prueba.

int main() {

  struct Node *root = NULL;   // Creamos un puntero a la raiz del arbol a crear.
  int root_value;
  int number_nodes;

  // Implementamos la entrada del usuario para crear un BST.

  // Asignamos el valor de la raiz del arbol.

  cout << "Ingrese el valor raiz para la generacion del arbol binario : ";
  cin >> root_value;
  root = insert(root, root_value);

  // Asignamos la cantidad de nodos que el arbol tendra.

  cout << "\nIngrese la cantidad de nodos para la generacion del arbol binario : ";
  cin >> number_nodes;

  cout << "\n";

  // Insertamos los valores de los nodos en el BST.

  for (int i = 0; i < number_nodes; i++) {
    int value;
    cout << "Ingrese el valor (" << i + 1 << ") : ";
    cin >> value;
    insert(root, value);
  }

  // Asignamos el valor que vamos a buscar en el BST.

  int value_to_search;
  cout << "Ingrese el valor que quiere buscar en el arbol : ";
  cin >> value_to_search;

  // Hacemos el output del programa con todo lo que se nos pide.

  if (iterativeSearch(root, value_to_search)) {
    cout << "\n";
    cout << "Nodo " << value_to_search << " encontrado!\n";
    cout << "La ruta del valor buscado desde el origen debe ser :\n";
    path_moves(moves);
    cout << "Los nodos que se visitan son los siguientes :";
    path_nodes(list_nodes);
    cout << "La representacion grafica del arbol es la siguiente :\n";
    printTree(root, 0);
  } else {
    cout << "\n";
    cout << "Nodo " << value_to_search << " no encontrado!\n";
  }
  
}