#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: the pointer to head of list.
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
listint_t *p1 = list;
listint_t *p2 = list;

if (list == NULL || list->next == NULL)
return (0);

while (p1 && p2 && p2->next)
{
p1 = p1->next;
p2 = p2->next->next;

if (p1 == p2)
return (1);
}

return (0);
}

