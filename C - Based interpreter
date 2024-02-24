#ifndef YOUR_INTERPRETER_H
#define YOUR_INTERPRETER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <setjmp.h>
#include "unity.h"

// Token types
// (Same as before)

// Token structure
typedef struct {
    int type;
    union {
        double num_val;
        char* str_val;
    } value;
} Token;

// Node structure for the syntax tree
typedef struct Node {
    int type;
    Token value;
    struct Node** children;
    int num_children;
} Node;

// Root node of the syntax tree
extern Node* root;

// Exception handling
typedef struct {
    int type;
    char message[256];
} Exception;

extern Exception current_exception;
extern jmp_buf exception_jump;

// Function prototypes
void notarize(const char* input_code);
void execute(Node* node);
void execute_block(Node* block);
void execute_if(Node* if_node);
void execute_while(Node* while_node);
void execute_try_catch(Node* try_catch_node);
void execute_task(Node* task_node);
double execute_expression(Node* expression);
void add_variable(const char* name, double num_val, const char* str_val);
void add_task(const char* name);
Node* create_node(int type, Token value);
int exception_occurred();
void clear_exception();
void raise_exception(int type, const char* format, ...);

// Lexer Rules
// (Same as before)

// Ignore Whitespace and Newlines
// (Same as before)

// Yacc/Bison Declarations
// (Same as before)

#endif  // YOUR_INTERPRETER_H
