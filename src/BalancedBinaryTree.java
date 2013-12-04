
public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) {
    	if( root == null ) return true;
    	if( root.left == null && root.right == null )
    		return true;
    	if( Math.abs(height(root.left) - height(root.right)) > 1 )
    		return false;
    	else 
    		return true;    	
    }
    public int height(TreeNode root) {
    	if( root == null ) return 0;
    	return 1 + Math.max(height(root.left), height(root.right));
    }
}
