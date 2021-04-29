#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert-node: Insert a number in a sorted singly linked list.
 * @head: Head of single linked list.
 * @number: Number to insert in linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new = NULL;
  listint_t *node1 = NULL;
  listint_t *node2 = NULL;

  if (head == NULL)
    return (NULL);
  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;
  new->next = NULL;
  node1 = *head;
  if (node1->next)
  {
    node2 = node1->next;
  }
  if (node2 == NULL)
  {
    add_nodeint_end(head, number);
    free(new);
    return (node1->next);
  }

  while (node1 != NULL) {
    if (node1->n <= number && node2->n >= number)
    {
      node1->next = new;
      new->next = node2;
      return new;
    }

    if (node1->next == NULL)
    {
      add_nodeint_end(head, number);
      free(new);
      return (node1->next);
    }
    node1 = node1->next;
    if (node1->next)
      node2 = node1->next;
    else
      node2 = NULL;
  }
  return 0;
}
