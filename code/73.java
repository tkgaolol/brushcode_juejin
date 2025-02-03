import java.util.ArrayList;
import java.util.List;

public class Main {
    static class Trie {

        static class TrieNode {
            TrieNode[] children;
            boolean isEnd;

            public TrieNode() {
                this.children = new TrieNode[75];
                this.isEnd = false;
            }
        }

        TrieNode root;

        public Trie() {
            root = new TrieNode();
        }

        public void insert(String word) {
            TrieNode trieNode = root;
            for (char c : word.toCharArray()) {
                int index = c - '0';
                if (trieNode.children[index] == null) {
                    trieNode.children[index] = new TrieNode();
                }
                trieNode = trieNode.children[index];
            }
            trieNode.isEnd = true;
        }

        public TrieNode findPrefix(String prefix) {
            TrieNode trieNode = root;
            for (char c : prefix.toCharArray()) {
                int index = c - '0';
                if (trieNode.children[index] == null) {
                    return null;
                }
                trieNode = trieNode.children[index];
            }
            return trieNode;
        }

        public List<String> search(String prefix) {
            TrieNode prefixNode = findPrefix(prefix);
            List<String> list = new ArrayList<>();
            if (prefixNode != null) {
                dfs(prefixNode, new StringBuilder(prefix), list);
            }
            return list;
        }

        private void dfs(TrieNode trieNode, StringBuilder sb, List<String> list) {
            if (trieNode.isEnd) {
                list.add(sb.toString());
            }
            for (int i = 0; i < 75; i++) {
                if (trieNode.children[i] != null) {
                    sb.append((char) ('0' + i));
                    dfs(trieNode.children[i], sb, list);
                    sb.delete(sb.length() - 1, sb.length());
                }
            }
        }
    }

    public static String solution(int num, String[] data, String input) {
        // Please write your code here
        Trie trie = new Trie();
        for (String s : data) {
            trie.insert(s);
        }
        List<String> search = trie.search(input);
        if (search.isEmpty()) {
            return "-1";
        } else {
            return String.join(",", search);
        }
    }

    public static void main(String[] args) {
        // You can add more test cases here
        String[] testData1 = { "select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id",
                "from_mobile" };

        System.out.println(solution(8, testData1, "f").equals("from,from_mobile"));
        System.out.println(solution(8, testData1, "wh").equals("where"));
        System.out.println(solution(8, testData1, "z").equals("-1"));
    }
}
