#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: list's head
 *
 * Return: 1 if palindrome 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = NULL, *slow = NULL, *mid = NULL, *prv = NULL, *nxt = NULL;
	listint_t *tmp1 = NULL, *tmp2 = NULL;

	/* Checks if list exists or is empty */
	if (head == NULL)
		return (0);

	else if (*head == NULL)
		return (1);

	/* Traverse the list to find mid point */
	fast = slow = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	mid = slow;

	/* Reverse second half of list */
	while (slow != NULL)
	{
		nxt = slow->next;
		slow->next = prv;
		prv = slow;
		slow = nxt;
	}
	/* Move slow back from NULL */
	slow = prv;
	/* Compare values of both list halves */
	tmp1 = *head;
	tmp2 = slow;

	while (tmp1 != mid && tmp2 != NULL)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	return (1);
}
