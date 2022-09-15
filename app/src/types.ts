export interface EventItem {
    id?: number;
    category: string;
    title: string;
    description: string;
    location: string;
    date: string;
    time: string;
    organization: string;
    catering: boolean;
    music: boolean;
    pets: number;
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
    catering: boolean;
    music: boolean;
    pets: number;

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
    catering: boolean;
    music: boolean;
    pets: number;
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
    catering: boolean;
    music: boolean;
    pets: number;
}