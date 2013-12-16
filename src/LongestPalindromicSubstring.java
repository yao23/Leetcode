
public class LongestPalindromicSubstring {
	public static void main(String[] args) {
		String s = "bb";
		String s2 = "abb";
		System.out.println(longestPalindrome(s));
		System.out.println(longestPalindrome(s2));
	}
	
	public static String longestPalindrome(String s) {
		if( s.length() == 0 )	return "";		
		String LongestStr = "";
		for( int i = 0; i < s.length() - 1; i++ ) {
			String OddStr = ExpandAroundCenter(s, i, i);
			if( OddStr.length() > LongestStr.length() )
				LongestStr = OddStr;
			String EvenStr = ExpandAroundCenter(s, i, i + 1);
			if( EvenStr.length() > LongestStr.length() )
				LongestStr = EvenStr;			
		}
		return LongestStr.toString();
    }
	private static String ExpandAroundCenter(String s, int l, int r) {
		int l_tmp = l, r_tmp = r;
		boolean FirstTime = true;

		while( l_tmp >= 0 && r_tmp < s.length() && s.charAt(l) == s.charAt(r) ) {
		    if( FirstTime )
		        FirstTime = false;
			l_tmp--;
			r_tmp++;
		}
			
		if( !FirstTime ) {
			l_tmp++;
			r_tmp--;
		}
		return s.substring(l_tmp, r_tmp + 1);
	}
}
