/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.2
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package com.twitter.ann.faiss;

public class InterruptCallback {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected InterruptCallback(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(InterruptCallback obj) {
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
        swigfaissJNI.delete_InterruptCallback(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public boolean want_interrupt() {
    return swigfaissJNI.InterruptCallback_want_interrupt(swigCPtr, this);
  }

  public static void clear_instance() {
    swigfaissJNI.InterruptCallback_clear_instance();
  }

  public static void check() {
    swigfaissJNI.InterruptCallback_check();
  }

  public static boolean is_interrupted() {
    return swigfaissJNI.InterruptCallback_is_interrupted();
  }

  public static long get_period_hint(long flops) {
    return swigfaissJNI.InterruptCallback_get_period_hint(flops);
  }

}
