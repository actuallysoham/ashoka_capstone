/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.twitter.ann.faiss;

public class ProgressiveDimClustering extends ProgressiveDimClusteringParameters {
  private transient long swigCPtr;

  protected ProgressiveDimClustering(long cPtr, boolean cMemoryOwn) {
    super(swigfaissJNI.ProgressiveDimClustering_SWIGUpcast(cPtr), cMemoryOwn);
    swigCPtr = cPtr;
  }

  protected static long getCPtr(ProgressiveDimClustering obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  @SuppressWarnings("deprecation")
  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        swigfaissJNI.delete_ProgressiveDimClustering(swigCPtr);
      }
      swigCPtr = 0;
    }
    super.delete();
  }

  public void setD(long value) {
    swigfaissJNI.ProgressiveDimClustering_d_set(swigCPtr, this, value);
  }

  public long getD() {
    return swigfaissJNI.ProgressiveDimClustering_d_get(swigCPtr, this);
  }

  public void setK(long value) {
    swigfaissJNI.ProgressiveDimClustering_k_set(swigCPtr, this, value);
  }

  public long getK() {
    return swigfaissJNI.ProgressiveDimClustering_k_get(swigCPtr, this);
  }

  public void setCentroids(FloatVector value) {
    swigfaissJNI.ProgressiveDimClustering_centroids_set(swigCPtr, this, FloatVector.getCPtr(value), value);
  }

  public FloatVector getCentroids() {
    long cPtr = swigfaissJNI.ProgressiveDimClustering_centroids_get(swigCPtr, this);
    return (cPtr == 0) ? null : new FloatVector(cPtr, false);
  }

  public void setIteration_stats(SWIGTYPE_p_std__vectorT_faiss__ClusteringIterationStats_t value) {
    swigfaissJNI.ProgressiveDimClustering_iteration_stats_set(swigCPtr, this, SWIGTYPE_p_std__vectorT_faiss__ClusteringIterationStats_t.getCPtr(value));
  }

  public SWIGTYPE_p_std__vectorT_faiss__ClusteringIterationStats_t getIteration_stats() {
    long cPtr = swigfaissJNI.ProgressiveDimClustering_iteration_stats_get(swigCPtr, this);
    return (cPtr == 0) ? null : new SWIGTYPE_p_std__vectorT_faiss__ClusteringIterationStats_t(cPtr, false);
  }

  public ProgressiveDimClustering(int d, int k) {
    this(swigfaissJNI.new_ProgressiveDimClustering__SWIG_0(d, k), true);
  }

  public ProgressiveDimClustering(int d, int k, ProgressiveDimClusteringParameters cp) {
    this(swigfaissJNI.new_ProgressiveDimClustering__SWIG_1(d, k, ProgressiveDimClusteringParameters.getCPtr(cp), cp), true);
  }

  public void train(long n, SWIGTYPE_p_float x, ProgressiveDimIndexFactory factory) {
    swigfaissJNI.ProgressiveDimClustering_train(swigCPtr, this, n, SWIGTYPE_p_float.getCPtr(x), ProgressiveDimIndexFactory.getCPtr(factory), factory);
  }

}
