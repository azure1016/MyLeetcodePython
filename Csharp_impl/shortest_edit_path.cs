using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
    {
        /// <summary>
        /// An undirected Graph data structure
        /// </summary>
        /// <typeparam name="T"></typeparam>
        public class Node<T>
        {
            // a better practice would be setting them as private, and write getter, setter for them
            public T word;
            public int level;
            public List<Node<T>> children;

            public Node(T word, int level)
            {
                this.word = word;
                this.level = level;
                this.children = new List<Node<T>> ();
            }
        }

        /// <summary>
        /// Return a list of strings in words that are one edit away from source
        /// </summary>
        /// <param name="source"></param>
        /// <param name="words"></param>
        /// <returns></returns>
        static private List<string> getWordsWithOneEdit(string source, List<string> words)
        {
            List<string> oneEdit = new List<string>();
            foreach (var word in words)
            {
                if (word.Length == source.Length)
                {
                    int diff = 0;
                    for (int i = 0; i < word.Length; i++)
                    {
                        if (word[i] != source[i])
                            diff++;
                    }

                    if (diff == 1)
                        oneEdit.Add(word);
                }
            }

            return oneEdit;
        }

        static public int ShortestPath(string source, string target, List<string> words)
        {
            Node<string> sourceNode = new Node<string> (source, 0);
            Queue<Node<string>> bfs = new Queue<Node<string>> ();
            // use a hash map to store the visited nodes for O(1) access
            HashSet<string> visited = new HashSet<string> ();
            bfs.Enqueue(sourceNode);
            visited.Add(source);
            while (bfs.Count > 0) 
            {
                var curNode = bfs.Dequeue();
                if (curNode.word == target)
                {
                    return curNode.level;
                }
                else {
                    List<string> neighbors = getWordsWithOneEdit(curNode.word, words);
                    foreach (var word in neighbors)
                    {
                        if (!visited.Contains(word)) {
                            visited.Add(word);
                            bfs.Enqueue(new Node<string>(word, curNode.level + 1));
                        }
                    }
                }
            }
            // if not found:
            return -1;
        }

        static void Main(string[] args)
        {
            //string source = "bit";
            //string target = "dog";
            //List<string> words = new List<string>() { "but", "put", "big", "pot", "pog", "dog", "lot" };

            string source2 = "no";
            string target2 = "go";
            List<string> words2 = new List<string>() { "to" };

            Console.WriteLine(string.Format("The length of the shortest series of edits that transforms from {0} to {1} is {2}", source2, target2,
                                            ShortestPath(source2, target2, words2)));

            System.Console.WriteLine("Practice makes Perfect!");
        }
    }

