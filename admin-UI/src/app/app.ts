import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
protected readonly title = signal('findex-search');
public searchQuery: string = '';
public typedText: string = '';
private fullText: string = "Findex.";

ngOnInit(){
  this.typeEffect()
}


  openSearch(){
    console.log(this.searchQuery);
  }

  async typeEffect() {
    const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));
    
    for (let i = 0; i <= this.fullText.length; i++) {
      this.typedText = this.fullText.substring(0, i);
      console.log(this.typedText);
      await sleep(100); // Adjust speed here (lower is faster)
    }
  }
}