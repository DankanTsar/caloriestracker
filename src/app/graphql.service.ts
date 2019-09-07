import { Injectable } from '@angular/core';
import { Apollo } from 'apollo-angular';
import { HttpLink } from 'apollo-angular-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import gql from 'graphql-tag';
import { UserType } from './types/user';

@Injectable({
  providedIn: 'root'
})
export class GraphqlService {
  public users: UserType[];
  public user: UserType;
  public createdUser: UserType;
  public updatedUser: UserType;
 
  constructor(private apollo: Apollo, httpLink: HttpLink) {
    apollo.create({
      link: httpLink.create({ uri: 'http://localhost:5000/graphql' }),
      cache: new InMemoryCache()
    })
  }

  public getUsers = () => {
    this.apollo.query({
      query: gql`query getUsers {
        allUsers {
          nodes {
            id
            name
          }
        }
      }`
    }).subscribe(result => {
      this.users = result.data as UserType[];
  console.log(this.users);
    })
  }
}

