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
	listint_t *start = NULL, *end = NULL;
	int len = 0, i, end_idx = 1;
	/* Check if linked list is NULL or empty */
	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);
	/* traverse list to determine lenght */
	start = *head;

	while (start != NULL)
	{
		++len;
		start = start->next;
	}

	start = *head;

	/* traverse and compare start and end nodes */
	for (i = 1; i <= (len / 2); ++i)
	{
		end = start;
		end_idx = i;

		while (end != NULL && end_idx <= (len - i))
		{
			end = end->next;
			++end_idx;
		}

		if (start->n != end->n)
			return (0);
		start = start->next;
	}

	/* list is palindromic */
	return (1);
}
