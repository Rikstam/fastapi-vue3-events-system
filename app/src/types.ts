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

export interface LoginUserPayload {
    username: string;
    password: string;
}

export interface CreateUserPayload {
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    password: string;
}

export type CreateUserResponse = {
    uuid: string;
    username: string;
    first_name: string;
    last_name: string;
}

export interface UserInfo {
    uuid: string;
    username: string;
    first_name: string;
    last_name: string;
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

export type LoginResponse = {
    access_token: string;
    bearer: string;
    userInfo: UserInfo;
}