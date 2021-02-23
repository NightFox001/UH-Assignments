#include <iostream>
#include <list>
#include "Node.h"
using namespace std;

int main(int argc, char* argv[]) {

  // I created a Node class with pointers to adjacent nodes for reusablitly and maintainability
  Node nodeS("S", 10);
  Node nodeA("A", 5);
  Node nodeB("B", 8);
  Node nodeC("C", 3);
  Node nodeD("D", 2);
  Node nodeE("E", 4);
  Node nodeF("F", 9);
  Node nodeG1("G1", 0);
  Node nodeG2("G2", 0);
  Node nodeH("H", 2);  

  Node* nodeSP = &nodeS;
  Node* nodeAP = &nodeA;
  Node* nodeBP = &nodeB;
  Node* nodeCP = &nodeC;
  Node* nodeDP = &nodeD;
  Node* nodeEP = &nodeE;
  Node* nodeFP = &nodeF;
  Node* nodeG1P = &nodeG1;
  Node* nodeG2P = &nodeG2;
  Node* nodeHP = &nodeH;

  // ajc to Node 'S'
  nodeS.addAdjacentNode(nodeAP);
  nodeS.addAdjacentNode(nodeBP);
  nodeS.addAdjacentNode(nodeFP);
  // ajc to Node 'A'
  nodeA.addAdjacentNode(nodeCP);
  nodeA.addAdjacentNode(nodeDP);
  nodeA.addAdjacentNode(nodeEP);
  // ajc to Node 'B'
  nodeB.addAdjacentNode(nodeEP);
  nodeB.addAdjacentNode(nodeG2P);
  // ajc to Node 'C'
  nodeC.addAdjacentNode(nodeDP);
  nodeC.addAdjacentNode(nodeSP);
  // ajc to Node 'D'
  nodeD.addAdjacentNode(nodeG1P);
  // ajc to Node 'E'
  nodeE.addAdjacentNode(nodeG2P);
  nodeE.addAdjacentNode(nodeHP);  
  // ajc to Node 'F'
  nodeF.addAdjacentNode(nodeDP);
    // ajc to Node 'G1'
  nodeG1.addAdjacentNode(nodeCP);
    // ajc to Node 'G2'
  nodeG2.addAdjacentNode(nodeBP);
  // ajc to Node 'H'
  nodeH.addAdjacentNode(nodeG2P);

  nodeS.printAdjacentNodes();
  nodeA.printAdjacentNodes();
  nodeB.printAdjacentNodes();
  nodeC.printAdjacentNodes();
  nodeD.printAdjacentNodes();
  nodeE.printAdjacentNodes();
  nodeF.printAdjacentNodes();
  nodeH.printAdjacentNodes();
  nodeG1.printAdjacentNodes();
  nodeG2.printAdjacentNodes();
  


  bool isGoalFound = false;
  string foundGoal = "";
  list<Node> OPEN;
  list<Node> CLOSED;
  list<Node> EXPANDED;

  // Establishing node S as the start node //
  OPEN.push_front(nodeS);
  nodeSP->setVisited(true);

  while (!OPEN.empty()){

    Node X = OPEN.front();
    OPEN.pop_front();
    EXPANDED.push_back(X);
    cout << "\n\nExpanding node " << X.getName() << endl;

    if (X.isGoalState() == true){
      cout << X.getName() << " is a goal state!\n";
      isGoalFound = true;
      foundGoal = X.getName();
      break;
    } 
    // if it is not the goal node, add it to closed list and add children that havent been visited yet to OPEN list 
    else { 
      CLOSED.push_back(X);
      vector<Node*> adjacentNodes = X.getAdjacentNodes();
      for (int i = 0; i < adjacentNodes.size(); ++i) {
        if (adjacentNodes[i]->getVisited() == true) {
          cout << "(skipping " << adjacentNodes[i]->getName() << ") ";
          continue;
        }
        else {
          cout << "(adding " << adjacentNodes[i]->getName() << " to OPEN) ";
          adjacentNodes[i]->setVisited(true);
          OPEN.push_back(*adjacentNodes[i]);
        }
      } // end for loop
    }
  } // end while loop

  cout << "\n\n\n";
  if (isGoalFound) {
    cout << "Goal Reached first: " << foundGoal << endl;
  } else { cout << "Goal not found.\n"; }
  cout << "Expanded states: ";
  while (!EXPANDED.empty()) {
    cout << EXPANDED.front().getName() << " ";
    EXPANDED.pop_front();
  }
  cout << "\nOPEN List: ";
  while (!OPEN.empty()) {
    cout << OPEN.front().getName() << " ";
    OPEN.pop_front();
  }
  cout << "\nCLOSED states: ";
  while (!CLOSED.empty()) {
    cout << CLOSED.front().getName() << " ";
    CLOSED.pop_front();
  }  
}