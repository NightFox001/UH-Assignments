#pragma once
#include <iostream>
#include <vector>
using namespace std;

class Node {
  private:
    string name;
    int value;
    int adjcantCount;
    bool visted = false;
    vector<Node*> adjacentNodes;
    Node* nodePtr = NULL;

  public:
  Node(string name, int value) {
    this->name = name;
    this->value = value;
    this->adjcantCount = 0;
  }

  void printName() {
    cout << this->name << endl;
  }

  string getName() { return this->name; }

  void addAdjacentNode(Node* adjacentNode) {
    nodePtr = adjacentNode;
    adjacentNodes.push_back(nodePtr);
  }

  void printAdjacentNodes() {
    cout << "Nodes adjacent to " << this->name << ": ";
    for (auto i: adjacentNodes) {
      cout << i->name << " "; 
    }
    cout << endl;
  }

  vector<Node*> getAdjacentNodes() {
    return adjacentNodes;
  }

  bool isGoalState() {
    if (this->name == "G1" || this->name == "G2") {
      return true;
    }
    return false;
  }

  void setVisited(bool value) {
    visted = value;
  }

  bool getVisited() {
    return visted;
  }

};