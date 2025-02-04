import java.util.LinkedList;
import java.util.Queue;
//树节点
class Node{
    int data;
    Node left;
    Node right;
    public Node(int data){
        this.data = data;
        left = null;
        right = null;
    }
}
public class Main {
     //记录暖炉个数
     static int result  = 0;
     public static int solution(int[] nodes) {
         // Please write your code here
         //因为result是静态变量，所以每次调用该方法时都初始化为0比较好
         //防止沿用之前的暖炉个数
         result = 0;
         //根据层序遍历的数组构造二叉树
         Node root = buildTree(nodes);
         //判断根节点是否已经供暖
         if(postorder_traversal(root) == 2){
             result++;
         }
         return result;
     }
     //后序遍历
     //每个节点有三种情况
     //0 -> 安装暖炉  1 -> 已供暖  2 -> 未供暖
     public static int postorder_traversal(Node root){
         //空节点的情况为被供暖
         if(root == null){
             return 1;
         }
         //左
         int left = postorder_traversal(root.left);
         //右
         int right = postorder_traversal(root.right);
         //根
         //如果两个叶子节点都已供暖
         if(left == 1 && right == 1){
             //返回当前节点未供暖
             return 2;
         }
         //如果两个叶子节点有一个未供暖
         if(left == 2 || right == 2){
             //安装暖炉给叶子节点供暖
             result++;
             return 0;
         }
         //如果两个叶子节点其中一个安装了暖炉
         if(left == 0 || right == 0){
             return 1;
         }
         //实际上不会走到这一步，上面已经将所有情况都考虑了
         return 1;
     }
     //根据层序遍历的数组构建二叉树
     public static Node buildTree(int[] nodes) {
         if (nodes == null || nodes.length == 0) {
             return null;
         }
         //构建根节点
         Node root = new Node(nodes[0]);
         //创建一个队列用于存储节点
         Queue<Node> queue = new LinkedList<>();
         queue.offer(root);
         //从数组的第二个元素开始
         int i = 1;
         while(!queue.isEmpty() && i < nodes.length){
             //从队列中取出一个节点
             Node current = queue.poll();
             //处理左子节点
             if(i < nodes.length && nodes[i] == 1){
                 current.left = new Node(nodes[i]);
                 queue.offer(current.left);
             }
             //移动指针
             i++;
             //处理右子节点
             if(i < nodes.length && nodes[i] == 1){
                 current.right = new Node(nodes[i]);
                 queue.offer(current.right);
             }
             //移动指针
             i++;
         }
         return root;
     }
 
    public static void main(String[] args) {
        //  You can add more test cases here
        int[] nodes1 = {1, 1, 0, 1, 1};
        int[] nodes2 = {1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1};
        int[] nodes3 = {1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1};
 
        System.out.println(solution(nodes1) == 1);
        System.out.println(solution(nodes2) == 3);
        System.out.println(solution(nodes3) == 3);
    }
}