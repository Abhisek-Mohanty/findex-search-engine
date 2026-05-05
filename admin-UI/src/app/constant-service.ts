import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { environment } from '../enviroment/enviroment';
import { map } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class ConstantService {
  API_URL: string = environment.API_URL;
  constructor(
    private http: HttpClient
  ){
  }
  getUrl(path: string, params: Array<any> = []) {
    return !params.length ? [this.API_URL, path].join('') : [[this.API_URL, path].join(''), params.join('/')].join('/');
  }

  getUrlByQuery(path: string, query: Array<Object>) {
    let url = [this.API_URL, path].join('');
    let queryString = query.map((o: any) => {
      return `${o.name}=${o.value}`;
    }).join('&');
    return [url, queryString].join('?');
  }

get(params?: any) {
  return this.http.get(this.getUrl("crawl"), {
    params: params,
    observe: 'response'
  }).pipe(
    map((resp: any) => {
      const count = resp.headers.get('X-Total-Count');
      return { count: parseInt(count, 10), data: resp.body.data };
    })
  );
}

}
