#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list to be checked
 *
 * Return: 0 if no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *cur;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list;
	cur = head->next;

	while (cur != NULL && cur->next != NULL && cur->next->next != NULL)
	{
		if (cur == head)
		{
			return (1);
		}
		cur = cur->next;
		head = head->next->next;
	}
	return (0);
}
