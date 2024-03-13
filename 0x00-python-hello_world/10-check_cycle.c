#include "lists.h"

/**
 * check_cycle - checks if a singly linked list is circular
 * @list: list to be checked
 *
 * Return: 1 if it's circular, and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *head = NULL, *cur = NULL;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list;
	cur = list->next;

	while (head != NULL && cur->next != NULL && cur->next->next != NULL)
	{
		if (cur == head)
			return (1);

		head = head->next;
		cur = cur->next->next;
	}
	return (0);
}
