/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author kevinoconnor
 */

import org.json.*;


public class OthelloAI {
    String[][] board = new String[8][8];
    String myColor;
    
    // Constructor
    public OthelloAI(String col) {
        myColor = col;
    }
    
    
    public static void main(String[] args){
        // Create OthelloAI object with given color and instantiate empty board.
        OthelloAI ai = new OthelloAI(args[1]);
        
        // Create and read in JSON object.
        JSONObject obj = new JSONObject(args[0]);
        JSONArray squares = obj.getJSONArray("squares");
        
        // Filling 2D board array with squares passed in.
        int length = squares.length();
        int j = 0;
        
        for (int i = 0; i < length; i++){
            ai.board[i][j] = squares.getString(i);
            if (j == 7){ j = 0; }
            else { j++; }
        }
        
    }
    
    
}
