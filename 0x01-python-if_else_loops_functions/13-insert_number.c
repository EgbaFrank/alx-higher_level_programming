#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to list
 * @number: number to be inserted
 *
 * Return: on success, address of new number, NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	/* create new node */
	listint_t *new = malloc(sizeof(listint_t));

	if (head == NULL || new == NULL)
	{
		free(new);
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	/* if the list is empty or number is less than first node */
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;

		return (new);
	}

	/* check for where to insert number */
	listint_t *cur = *head;

	while (cur->next != NULL && number > cur->next->n)
		cur = cur->next;

	new->next = cur->next;
	cur->next = new;

	return (new);
}
