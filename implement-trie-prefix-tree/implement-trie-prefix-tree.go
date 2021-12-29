type Trie struct {
    Children map[rune]*Trie
    EndHere bool
}


func Constructor() Trie {
    return Trie{Children: map[rune]*Trie{}, EndHere: false}
}


func (this *Trie) Insert(word string)  {
    node := this
    for _, char := range word {
        _, endhere := node.Children[char]
        if endhere == false {
            node.Children[char] = &Trie{Children: map[rune]*Trie{}, EndHere: false}   
        }
        node = node.Children[char]
    }
    node.EndHere = true
}


func (this *Trie) Search(word string) bool {
    node := this
    for _, char := range word {
        _, endhere := node.Children[char]
        if endhere == false {
            return false
        }
        node = node.Children[char]
    }
    return node.EndHere
}


func (this *Trie) StartsWith(prefix string) bool {
    node := this
    for _, char := range prefix {
        _, endhere := node.Children[char]
        if endhere == false {
            return false
        }
        node = node.Children[char]
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */