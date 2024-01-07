#ifndef LISTS_H
#define LISTS_H

/**
 * struct list_s - linked list singly
 * @x: int
 * @next: pointing to next node
 *
 * Description: singly linked list node structure
 * for alx project
 */
typedef struct list_s
{
    int x;
    struct list_s *next;
} list_t;

size_t print_list(const list_t *h);
list_t *add_nodeint_end(list_t **head, const int x);
void free_list(list_t *head);

int is_palindrome(list_t **head);
