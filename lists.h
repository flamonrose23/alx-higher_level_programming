#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @x: integer
 * @nxt: pointing to next node
 *
 * Description: singly linked list node structure
 * for Holbert Alx project
 */
typedef struct listint_s
{
    int x;
    struct listint_s *nxt;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int x);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
