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
	listint_t *head, *current;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list;
	current = head->next;

	while (current != NULL && current->next != NULL && current->next->next != NULL)
	{
		if (current == head)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
