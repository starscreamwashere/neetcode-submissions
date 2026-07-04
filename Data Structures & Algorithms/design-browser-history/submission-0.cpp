#include <string>
#include <vector>
#include <algorithm>

class BrowserHistory {
private:
    std::vector<std::string> history;
    int currIdx;
    int maxIdx;

public:
    BrowserHistory(std::string homepage) {
        history.push_back(homepage);
        currIdx = 0;
        maxIdx = 0;
    }
    
    void visit(std::string url) {
        currIdx++;
        
        // If we are overwriting old forward history, reuse the vector slots
        if (currIdx < history.size()) {
            history[currIdx] = url;
        } else {
            // Otherwise, expand the vector
            history.push_back(url);
        }
        
        // Wipe out any forward history by capping maxIdx at our current position
        maxIdx = currIdx;
    }
    
    std::string back(int steps) {
        // Move back, but don't go past the homepage (index 0)
        currIdx = std::max(0, currIdx - steps);
        return history[currIdx];
    }
    
    std::string forward(int steps) {
        // Move forward, but don't go past the max valid history index
        currIdx = std::min(maxIdx, currIdx + steps);
        return history[currIdx];
    }
};