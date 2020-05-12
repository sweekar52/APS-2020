#include<iostream>

using namespace std;


class linkedList{
    private:
        struct node{
            int data;
            node *next;
            node *prev;
        };
        typedef node NODE;

        int len;
        NODE *head;
        NODE *tail;

        NODE* getNode(int num){
            NODE *temp = new NODE;
            temp->data = num;
            temp->next = NULL;
            temp->prev = NULL;
            return temp;
        }

    public:

        linkedList(){
            this->head = getNode(0);
            this->tail = getNode(0);
            this->head->next = this->tail;
            this->tail->prev = this->head;
        }

        void pushFront(int x);
        void pushBack(int x);
        int popFront();
        int popBack();
        int getSize();
        void print();
};

int linkedList::getSize(){
    return this->head->data;
}

void linkedList::pushFront(int x){
    NODE *newNode = getNode(x);
    newNode-> prev = this->head;
    newNode->next = this->head->next;
    this->head->next->prev=newNode;
    this->head->next = newNode;
    this->head->data++;
}

int linkedList::popFront(){
    if(this->head->data == 0){
        throw underflow_error("No more elements to pop");
    }
    NODE *temp = this->head->next;
    int data = temp->data;
    this->head->next = temp->next;
    this->head->next->prev = this->head;
    free(temp);
    this->head->data --;
    return data;
}

int linkedList::popBack(){
    if(this->head->data == 0){
        throw underflow_error("No more elements to pop");
    }
    NODE *temp = this->tail->prev;
    int data = temp->data;
    this->tail->prev = temp->prev;
    this->tail->prev->next = this->tail;
    free(temp);
    this->head->data --;
    return data;
}

void linkedList::pushBack(int x){
    NODE *newNode = getNode(x);
    newNode->next = this->tail;
    newNode->prev = this->tail->prev;
    this->tail->prev->next = newNode;
    this->tail->prev = newNode;
    this->head->data++;
}

void linkedList::print(){
    NODE *temp = this->head->next;
    while(temp!=this->tail){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
}

int main(){
    linkedList ll;
    ll.pushBack(5);
    ll.pushBack(6);
    ll.pushBack(7);
    ll.pushBack(8);
    ll.pushFront(1);
    ll.print();
    cout<<"\nPOPF:"<<ll.popFront()<<endl;
    cout<<"\nPOPB:"<<ll.popBack()<<endl;
    ll.print();
    cout<<"\n"<<ll.getSize();
    return 0;
}