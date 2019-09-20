using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PrampTest
{
    class Program
    {
        /// <summary>
        /// An undirected Graph data structure
        /// </summary>
        /// <typeparam name="T"></typeparam>
        public class Graph<T>
        {
            List<T> vertices;
            Dictionary<T, List<T>> adjacent;

            public Graph()
            {
                vertices = new List<T>();
                adjacent = new Dictionary<T, List<T>>();
            }

            public void AddVertex(T vertex)
            {
                if (!vertices.Contains(vertex))
                {
                    vertices.Add(vertex);
                }

                if (!adjacent.Keys.Contains(vertex))
                {
                    List<T> adjList = new List<T>();
                    adjacent.Add(vertex, adjList);
                }
            }

            /// <summary>
            /// Return true if the input vertex exists
            /// in the graph
            /// </summary>
            /// <param name="vertex"></param>
            /// <returns></returns>
            public bool HasVertex(T vertex)
            {
                return vertices.Contains(vertex);
            }

            public void AddEdge(T from, T to)
            {
                if (!adjacent.Keys.Contains(from))
                {
                    AddVertex(from);
                }
                // Hi, you don't have to copy out the adjacent[from] as 'asjList', this would cost
                // extra space and time.
                /* List<T> adjList = adjacent[from];
                if (!adjList.Contains(to))
                {
                    adjList.Add(to);
                    adjacent[from] = adjList;
                }*/
                if (!adjacent[from].Contains(to))
                {
                    adjacent[from].Add(to);
                }
            }

            /// <summary>
            /// Return a list of vertices that has an edge
            /// from the input vertex
            /// </summary>
            /// <param name="vertex"></param>
            /// <returns></returns>
            public List<T> GetEdges(T vertex)
            {
                return adjacent[vertex];
            }
        }


        static private Graph<string> constructGraph(string source, List<string> words)
        {
            Graph<string> graph = new Graph<string>();
            Queue<string> addChildrenTo = new Queue<string>();

            graph.AddVertex(source);
            addChildrenTo.Enqueue(source);
            while (addChildrenTo.Count > 0)
            {
                var parentCount = addChildrenTo.Count;
                for (int i = 0; i < parentCount; i++)
                {
                    var curParent = addChildrenTo.Dequeue();

                    var children = getWordsWithOneEdit(curParent, words);
                    foreach (var child in children)
                    {
                        graph.AddVertex(child);
                        graph.AddEdge(curParent, child);
                        words.Remove(child);
                        addChildrenTo.Enqueue(child);
                    }
                }
            }

            return graph;
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
            int pathLength = -1;

            var graph = constructGraph(source, words);
            if (graph.HasVertex(target))
            {
                pathLength = 0;
                Queue<string> nodeToTraverse = new Queue<string>();
                List<string> vistedNodes = new List<string>();
                nodeToTraverse.Enqueue(source);
                vistedNodes.Add(source);
                while (nodeToTraverse.Count > 0)
                {
                    var parentCount = nodeToTraverse.Count;
                    for (int i = 0; i < parentCount; i++)
                    {
                        var curParent = nodeToTraverse.Dequeue();
                        if (curParent == target)
                            return pathLength;
                        var children = graph.GetEdges(curParent).Except(vistedNodes).ToList();
                        foreach (var child in children)
                        {
                            nodeToTraverse.Enqueue(child);
                            vistedNodes.Add(child);
                        }
                    }
                    pathLength++;
                }
            }

            return pathLength;
        }

        static void Main(string[] args)
        {
            string source = "bit";
            string target = "dog";
            List<string> words = new List<string>() { "but", "put", "big", "pot", "pog", "dog", "lot" };

            //string source = "no";
            //string target = "go";
            //List<string> words = new List<string>() { "to" };

            Console.WriteLine(string.Format("The length of the shortest series of edits that transforms from {0} to {1} is {2}", source, target,
                                            ShortestPath(source, target, words)));

            System.Console.WriteLine("Practice makes Perfect!");
        }
    }
}
