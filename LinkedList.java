import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Node {
	public int value;
	public Node next;

    public Node(int value) {
        this.value = value;
        this.next = null;
	}

	@Override
	public String toString() {
        return Integer.toString(value);
	}
}

public class LinkedList {
	private Node head;

	public LinkedList(List<Integer> ls) {
        this.head = null;
        if(ls != null) {
			int value = ls.remove(0);
            Node node = new Node(value);
            this.head = node;
            for(int element : ls) {
                node.next = new Node(element);
                node = node.next;
			}
		}
	}

    public void append(int value) {
        Node temp = new Node(value);
        if(this.head == null) {
            this.head = temp;
        } else {
            Node current = this.head;
            while(current.next != null) {
                current = current.next;
            }
            current.next = temp;
        }
    }

    public void delete_at_index(int index) {
        if(this.head != null) {
            if(index == 0) {
                this.head = this.head.next;
            } else {
                Node temp = this.head;
                while(temp != null && index > 1) {
                    temp = temp.next;
                    index = index - 1;
                }
                if(index == 1 && temp.next != null) {
                    temp.next = temp.next.next;
                }
           }
       }
    }

    public void prepend(int value) {
        Node node = new Node(value);
        node.next = this.head;
        this.head = node;
    }

    @Override
    public String toString() {
        Node node = this.head;
        String result = "";
        while(node != null) {
            result = result  + node.value + " -> ";
            node = node.next;
        }
        result = result + "None";
        return result;
    }

	public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(20);
        nums.add(30);
    	LinkedList llist = new LinkedList(nums);
    	System.out.printf("\noriginal llist:\n\t %s\n", llist);

        llist.prepend(10);
        llist.append(40);
        System.out.printf("\nllist 10 through 40:\n\t %s\n", llist);

        llist.delete_at_index(0);
        System.out.printf("\nnode 0 removed:\n\t %s\n", llist);
    
        llist.delete_at_index(2);
        System.out.printf("\nnode 2 removed:\n\t %s\n", llist);

        nums.clear();
        for(int i=11; i<=55; i+=11) {
            nums.add(i);
        }
        llist = new LinkedList(nums);
        System.out.printf("\nrefreshed the llist:\n\t %s\n", llist);

        llist.delete_at_index(20);
        System.out.printf("\nnode 20 removed:\n\t %s\n", llist);

        llist.delete_at_index(1);
        System.out.printf("\nnode 1 removed:\n\t %s\n", llist);

        llist.delete_at_index(1);
        System.out.printf("\nnode 1 removed:\n\t %s\n", llist);

        llist.delete_at_index(0);
        System.out.printf("\nnode 0 removed:\n\t %s\n", llist);

    }

}