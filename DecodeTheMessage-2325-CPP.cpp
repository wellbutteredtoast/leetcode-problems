// LeetCode Problem #2325 -- Decode the Message
// Language: C++
// Runtime: 2ms
// Memory: 10.10mb
// Date: 17 March, 2025

#include <iostream>
#include <unordered_set>
#include <vector>
#include <map>

using namespace std;

string decodeMessage(string key, string message) {

    unordered_set<char> seen;
    vector<char> subTable;

    // Extract the unique characters in order of appearance
    for (char c : key) {
        if (c != ' ' && seen.find(c) == seen.end()) {
            seen.insert(c);
            subTable.push_back(c);
        }
    }

    // Create the subtitute map with the key
    map<char, char> decodeMap;
    char currentLetter = 'a';
    for (char c : subTable) {
        decodeMap[c] = currentLetter++;
    }

    // Decode and return the message passed
    string decodedMessage;
    for (char c : message) {
        if (c == ' ') {
            decodedMessage += ' ';
        } else {
            decodedMessage += decodeMap[c];
        }
    }

    return decodedMessage;
}
