export interface EventItem {
    id?: number;
    category: string;
    title: string;
    description: string;
    location: string;
    date: string;
    time: string;
    organization: string;
}

export interface UserItem {
    user: string;
}

export type GetEventsResponse = {
    id: number;
    category: string;
    title: string;
    description: string;
    location: string;
    date: string;
    time: string;
    organization: string;
}[]

export type GetEventResponse = {
    id: number;
    category: string;
    title: string;
    description: string;
    location: string;
    date: string;
    time: string;
    organization: string;
}

export type CreateEventResponse = {
    id: number;
    category: string;
    title: string;
    description: string;
    location: string;
    date: string;
    time: string;
    organization: string;
}