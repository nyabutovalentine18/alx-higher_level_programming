#include "lists.h"

/**
*insert_node - inserts a number into a sorted singly linked list
*@head: pointer to the first element
*
*@number: a number to be inserted
*
*Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{

listint_t *ptr, *pp;
ptr = *head;
ptr = malloc(sizeof(listint_t));
if (ptr == NULL)
{
return (NULL);
}
pp = *head;
pp->n = number;

if (pp == NULL || number <= pp->n)
{
ptr->next = pp;
*head = ptr;
return (ptr);
}
while (pp && pp->next && pp->next->n < number)
pp = pp->next;
ptr->next = pp->next;
pp->next = ptr;
return (ptr);
}




