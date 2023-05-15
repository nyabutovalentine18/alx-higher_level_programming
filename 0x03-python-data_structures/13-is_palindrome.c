#include "lists.h"
/**
*reverse_listint - reverses the singly linked list
*
*@head: double pointer to the first node of the list
*
*Return: pointer
*/
void reverse_listint(listint_t **head)
{
listint_t *pv = NULL, *next = NULL, *ct = *head;

while (ct)
{
next = ct->next;
ct->next = pv;
pv = ct;
ct = next;
}

*head = pv;
}

/**
*is_palindrome - checks if the singly linked list is palindrome
*
*@head: double pointer to the first node of the list
*
*Return: 1 if terminates, others 0
*/
int is_palindrome(listint_t **head)
{
listint_t *ft = *head;
listint_t *st = *head;
listint_t *tp = *head;
listint_t *dp = NULL;

if (*head == NULL || (*head)->next == NULL)
{
return (1);
}

while (1)
{
ft = ft->next->next;
if (!ft)
{
dp = st->next;
break;
}
if (!ft->next)
{
dp = st->next->next;
break;
}
st = st->next;
}

reverse_listint(&dp);
while (dp && tp)
{
if (tp->n == dp->n)
{
dp = dp->next;
tp = tp->next;
}
else
return (0);
}
if (dp == NULL)
return (1);
return (0);
}
