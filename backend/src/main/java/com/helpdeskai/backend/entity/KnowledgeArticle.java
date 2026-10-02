package com.helpdeskai.backend.entity;
import jakarta.persistence.*;


@Entity
public class KnowledgeArticle {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    @Column(columnDefinition = "TEXT")
    private String content;
    private String tags;
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public String getTitle() { return this.title; }
    public void setTitle(String title) { this.title = title; }
    public String getContent() { return this.content; }
    public void setContent(String content) { this.content = content; }
    public String getTags() { return this.tags; }
    public void setTags(String tags) { this.tags = tags; }
}