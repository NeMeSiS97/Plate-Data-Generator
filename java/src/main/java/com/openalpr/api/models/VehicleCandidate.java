/*
 * OpenALPR Cloud API
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 2.0.1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.openalpr.api.models;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.math.BigDecimal;

/**
 * VehicleCandidate
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2017-06-29T08:43:22.221-04:00")
public class VehicleCandidate {
  @SerializedName("name")
  private String name = null;

  @SerializedName("confidence")
  private BigDecimal confidence = null;

  public VehicleCandidate name(String name) {
    this.name = name;
    return this;
  }

   /**
   * name of value
   * @return name
  **/
  @ApiModelProperty(value = "name of value")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public VehicleCandidate confidence(BigDecimal confidence) {
    this.confidence = confidence;
    return this;
  }

   /**
   * confidence of value (percent)
   * @return confidence
  **/
  @ApiModelProperty(value = "confidence of value (percent)")
  public BigDecimal getConfidence() {
    return confidence;
  }

  public void setConfidence(BigDecimal confidence) {
    this.confidence = confidence;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleCandidate vehicleCandidate = (VehicleCandidate) o;
    return Objects.equals(this.name, vehicleCandidate.name) &&
        Objects.equals(this.confidence, vehicleCandidate.confidence);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, confidence);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleCandidate {\n");
    
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    confidence: ").append(toIndentedString(confidence)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
  
}

